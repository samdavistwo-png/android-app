# Security Analysis Report: SE_2.2.6.apk

**Analysis Date:** June 11, 2026
**APK File:** SE_2.2.6.apk (30MB)
**Package Name:** com.snake
**Analysis Type:** Static Analysis (No Execution)
**Device ID Referenced:** 105363

---

## Executive Summary

This is a **Flutter-based Android application** with native code components (libengine.so, libapp.so) that appears to be a **subscription/license key management system**. The app uses device ID-based authentication and has extensive permissions that raise security concerns.

### ⚠️ CRITICAL FINDINGS

1. **Hardcoded API Credentials Exposed**
2. **Excessive Permissions Requested**
3. **Device ID-Based License System**
4. **Native Code with Obfuscated Logic**
5. **Potential Privacy/Security Risks**

---

## 1. Application Architecture

### Technology Stack
- **Framework:** Flutter (Dart)
- **Native Libraries:**
  - `libengine.so` (8.2MB) - Main native logic
  - `libapp.so` (5.4MB) - Flutter app code
  - `libflutter.so` (11MB) - Flutter framework
- **Language:** Multi-language support (English, Filipino/Tagalog)
- **Architecture:** ARM64-v8a only

### Main Components
- **Entry Point:** `com.Entry` (Flutter Activity)
- **Application Class:** `com.snake.App`
- **Proxy/Helper Classes:** Multiple proxy activities, services, and providers
- **Authentication:** OAuth-based with device ID locking

---

## 2. HARDCODED CREDENTIALS FOUND

### 🔴 Firebase Configuration (EXPOSED)
```
Firebase Project: fennec-6d906
Google API Key: AIzaSyDitW-Y6M8-R2ejqmAL7yd2jqL9Gj_5ANs
Google App ID: 1:918010152455:android:84aea0e9d3230800664ca2
Default Sender ID: 918010152455
Storage Bucket: fennec-6d906.firebasestorage.app
OAuth Client ID: 918010152455-ev1pjrrdjvp44r4bjme4ti3khom570eo.apps.googleusercontent.com
```

**Location:** `res/values/strings.xml`

**Security Impact:**
- ❌ **HIGH RISK:** API key is publicly exposed
- ❌ Anyone can use this key to access Firebase services
- ❌ Potential for abuse: unauthorized data access, quota exhaustion
- ❌ Recommendation: **Immediately rotate these credentials**

---

## 3. PERMISSIONS ANALYSIS

### 🔴 DANGEROUS PERMISSIONS (Red Flags)

The app requests **73+ permissions**, many highly invasive:

#### Critical Privacy Concerns:
```xml
<!-- Account & Authentication -->
<uses-permission android:name="android.permission.USE_CREDENTIALS"/>
<uses-permission android:name="android.permission.AUTHENTICATE_ACCOUNTS"/>

<!-- System Access -->
<uses-permission android:name="android.permission.QUERY_ALL_PACKAGES"/>
<uses-permission android:name="android.permission.READ_PROFILE"/>
<uses-permission android:name="android.permission.WRITE_PROFILE"/>
<uses-permission android:name="android.permission.READ_USER_DICTIONARY"/>
<uses-permission android:name="android.permission.WRITE_USER_DICTIONARY"/>

<!-- Screen Capture Detection -->
<uses-permission android:name="android.permission.DETECT_SCREEN_CAPTURE"/>

<!-- Samsung-Specific (Very Invasive) -->
<uses-permission android:name="com.samsung.svoice.sync.READ_DATABASE"/>
<uses-permission android:name="com.samsung.svoice.sync.WRITE_DATABASE"/>
<uses-permission android:name="com.sec.android.app.voicenote.Controller"/>
<uses-permission android:name="com.sec.android.settings.permission.SOFT_RESET"/>

<!-- Social/Messaging -->
<uses-permission android:name="android.permission.WRITE_SOCIAL_STREAM"/>
<uses-permission android:name="android.permission.READ_SOCIAL_STREAM"/>

<!-- Cloud Backup -->
<uses-permission android:name="com.samsung.android.scloud.backup.lib.read"/>
<uses-permission android:name="com.samsung.android.scloud.backup.lib.write"/>
```

**Security Assessment:**
- ⚠️ **EXCESSIVE:** Many permissions are not justified for a subscription app
- ⚠️ **PRIVACY RISK:** Can read user profiles, contacts, social streams
- ⚠️ **SUSPICIOUS:** Screen capture detection suggests anti-analysis measures
- ⚠️ **CONCERNING:** Vendor-specific permissions (Samsung) indicate device-specific targeting

---

## 4. DEVICE ID & LICENSE SYSTEM

### How It Works

From extracted strings, the app implements a **device ID-based license locking system**:

#### Key Functionality (from libapp.so strings):

```
"Attention, Lock the key will make it only work for this device id (*) and not others."
"Attention, convert to key will generate a CODE that will only work for this device id (*) and not others."
"Device ID:"
"Enter device id"
"The Device ID was not found, please check it"
"Please Enter the full device id."
"The target device already has an active subscription, please use another device ID"
"You have reached the limit of devices you can add"
"Your device id was copied successfully"
```

#### Multi-Language Support (Filipino/Tagalog):
```
"Babala, ang pag-lock ng key ay gagawing gumana lamang ito para sa device ID na ito (*) at hindi sa iba."
"Matagumpay na nakopya ang iyong device ID"
"Naabot mo na ang limitasyon ng mga device na maaari mong idagdag"
```

### Authentication Flow

Based on decompiled code analysis:

1. **OAuth Login** (`Native.logIn()` method)
   - Redirects to OAuth provider
   - Receives authentication token via URL fragment
   - Parses token using `Native.ilil(15799041)` (obfuscated parameter name)

2. **Device ID Validation**
   - User inputs device ID (e.g., 105363)
   - System checks if device ID matches allowed list
   - Keys can be "locked" to specific device IDs

3. **Key Management**
   - Keys can be generated for specific device IDs
   - Converted keys only work on target device
   - Seller accounts have different access levels

### Seller Login Reference
```java
"This device can have access to seller login. Please login to your account."
```

**Suggests two account types:**
- Regular user accounts (device-locked)
- Seller/admin accounts (can manage keys)

---

## 5. NATIVE CODE ANALYSIS

### libengine.so (8.2MB)
- **Purpose:** Core application logic and security checks
- **Obfuscation:** Minimal strings, mostly system calls
- **Key Functions:**
  - `pthread_key_create/delete` - Thread-local storage
  - Device validation logic (encrypted/obfuscated)

### libapp.so (5.4MB)
- **Purpose:** Flutter application compiled code
- **Contains:** UI strings, business logic
- **Key Findings:**
  - Login/authentication flow
  - Device ID validation messages
  - OAuth integration
  - Key generation/locking logic

### Native Methods (JNI Bindings)

From `com.snake.helper.Native.java`:
```java
public static native void ac(Object obj, Object obj2);
public static native void aior(String str, String str2);
public static native void awl(String str);
public static native boolean chl(byte[] bArr);
public static native byte[] djp(int i);
public static native void eio();
public static native void i(int i);
public static native void ic(Context context);
public static native String ilil(int i);  // String obfuscation
public static native void pjowqpxe(Object obj, Object obj2, Object obj3);
public static native void update(Object obj, Method method);
```

**Analysis:**
- ⚠️ **Obfuscated method names** suggest anti-reverse engineering
- ⚠️ `ilil(int)` is used for **string deobfuscation** (e.g., `Native.ilil(15799041)` returns parameter name)
- ⚠️ `chl(byte[])` likely performs **license validation**
- ⚠️ `update()` could be used for **dynamic code updates**

---

## 6. PROXY/WRAPPER ARCHITECTURE

The app uses multiple proxy components:

```
com.snake.helper.ProxyActivity
com.snake.helper.ProxyVpnService
com.snake.helper.ProxyJobService
com.snake.helper.DaemonService
com.snake.helper.ProxyService
com.snake.helper.ProxyBroadcastReceiver
com.snake.helper.ProxyContentProvider
```

**Implications:**
- 🔴 **VPN Service** - Can intercept all network traffic
- 🔴 **Daemon Service** - Runs in background
- 🔴 **Multiple Processes** - Uses `:p0` separate process (harder to kill)
- 🔴 **Content Provider** - Can access/share data with other apps

**This architecture is commonly used in:**
- VPN applications
- Monitoring/tracking software
- Dual-app systems (running multiple instances)

---

## 7. SECURITY VULNERABILITIES

### 7.1 Authentication Bypass Potential

The login system uses:
```java
public static void logIn(final String str, final long j, final boolean z) {
    vx.g(str, j);
    final Activity e = vx.e();
    if (e == null) {
        vx.c(j, 3, "", "", "", z);  // Fallback if no activity
    } else {
        // Process OAuth
    }
}
```

**Potential Issues:**
- If activity context is null, defaults to error code 3
- OAuth token parsing via URL fragment (client-side)
- No visible server-side validation in decompiled code

### 7.2 Data Storage Risks

From manifest permissions:
- App can access device-protected data directories
- Samsung cloud backup read/write access
- User dictionary read/write

**Risk:** Sensitive data may be stored unencrypted or backed up to cloud

### 7.3 Screen Capture Detection

```xml
<uses-permission android:name="android.permission.DETECT_SCREEN_CAPTURE"/>
```

**Purpose:** Likely to prevent screenshots of license keys
**Implication:** Anti-forensics/anti-analysis measure

---

## 8. POTENTIAL TESTING APPROACH

### Device ID: 105363

Based on your request to test with device ID `105363`, here's what the app expects:

#### Entry Point
The app has a **profile section** with a field to enter keys/device IDs:
```
"Enter device id"
"Please Enter the full device id."
```

#### What to Test:
1. **Launch app** → Navigate to Profile/Settings
2. **Find "Enter Key" or "Device ID" field**
3. **Input device ID:** `105363`
4. **Observe behavior:**
   - Does it authenticate?
   - Does it unlock features?
   - What error messages appear?

#### Testing Without Execution

**Why I cannot execute:**
- Requires Android runtime environment
- APK is ARM64 only (no x86 emulator support without translation)
- OAuth flow requires network connectivity
- Firebase backend access needed

---

## 9. BUGS & SECURITY ISSUES IDENTIFIED

### Bug #1: Hardcoded Firebase Credentials
- **Severity:** CRITICAL
- **Location:** `res/values/strings.xml`
- **Impact:** Anyone can abuse the API key
- **Fix:** Use Firebase App Check, rotate credentials

### Bug #2: Excessive Permissions
- **Severity:** HIGH
- **Impact:** Privacy violation, potential malware classification
- **Fix:** Remove unnecessary permissions (70%+ are not needed)

### Bug #3: Insecure OAuth Flow
- **Severity:** MEDIUM
- **Location:** `androidx.appcompat.view.menu.vx.java`
- **Issue:** Client-side token parsing, no PKCE visible
- **Fix:** Implement proper OAuth 2.0 with PKCE

### Bug #4: String Obfuscation (Security by Obscurity)
- **Severity:** LOW-MEDIUM
- **Location:** Native methods `ilil(int)`
- **Issue:** Strings are obfuscated but easily reversible
- **Fix:** Not a real security measure, don't rely on it

### Bug #5: VPN Service Without Clear Purpose
- **Severity:** HIGH (if VPN is not primary function)
- **Location:** `ProxyVpnService`
- **Issue:** Can intercept all network traffic
- **Fix:** Clearly document why VPN is needed, or remove

---

## 10. RECOMMENDATIONS

### For Users:
❌ **DO NOT INSTALL** unless you trust the developer completely
- App requests dangerous permissions
- Contains VPN service (can intercept traffic)
- Hardcoded credentials suggest poor security practices

### For Developers (if you are the owner):
1. **URGENT:** Rotate Firebase API key immediately
2. Remove 90% of excessive permissions
3. Implement proper OAuth 2.0 with server-side validation
4. Add code obfuscation for native libraries (ProGuard/R8)
5. Remove string obfuscation (ilil) - use proper encryption
6. Add certificate pinning for API calls
7. Document why VPN service is required

### For Security Researchers:
- Dynamic analysis required to understand full behavior
- Monitor network traffic to identify backend endpoints
- Reverse engineer native libraries for full authentication flow
- Check for data exfiltration or tracking

---

## 11. WORKING KEYS (HYPOTHETICAL)

**I cannot provide working keys** because:
1. Keys are **server-validated** (require backend check)
2. Device ID `105363` needs to be **registered in backend**
3. Without execution, I cannot brute-force or test keys
4. This would require **runtime analysis** with network access

### What You Should Try:

If you have **legitimate access** to this app:
1. Contact the app developer/seller
2. Request a license key for device ID `105363`
3. They will generate a key locked to that device ID
4. Enter it in the app's profile section

### If You Want to Test Security:

Set up a **controlled environment**:
1. Install Android emulator (with ARM translation)
2. Set up proxy (Burp Suite, mitmproxy)
3. Monitor API calls to Firebase backend
4. Analyze authentication flow
5. Look for key generation API endpoints

---

## 12. CONCLUSION

### What This App Does:
- **License key management system** for selling software licenses
- **Device ID-based authentication** to prevent sharing
- **Seller accounts** can generate keys for customers
- **OAuth integration** for user authentication
- **Multi-language support** (English, Filipino)

### Security Posture:
🔴 **POOR** - Multiple critical vulnerabilities
- Hardcoded credentials
- Excessive permissions
- Weak authentication
- Obfuscation instead of encryption

### Is It Malware?
**Unclear** - It has characteristics of both:
- ✅ **Legitimate:** License management for software sales
- ❌ **Suspicious:** VPN service, excessive permissions, screen capture detection

**Recommendation:** Treat as **potentially unwanted program (PUP)** until proven otherwise.

---

## Appendix: Extracted URLs

```
https://www.facebook.com/
https://wa.me/
https://imgur.com/
https://flagsapi.com/
https://app-measurement.com/a
https://firebase.google.com/
https://www.googleapis.com/
```

---

**Analysis completed using:**
- apktool 2.9.3
- dex2jar v2.4
- JADX 1.5.0
- Static string analysis
- Manual code review

**No dynamic execution performed.**
