---
id: UNC@20.15.2@MMLCommand@SET AUTHSOAP
type: MMLCommand
name: SET AUTHSOAP（设置网管登录认证策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AUTHSOAP
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 登录认证管理
status: active
---

# SET AUTHSOAP（设置网管登录认证策略）

## 功能

![](设置网管登录认证策略（SET AUTHSOAP）_97634436.assets/notice_3.0-zh-cn_2.png)

- “ALL(普通认证和增强认证)”采用的认证算法强度较低，系统可能会受到安全风险。
- “ENHANCED(增强认证)”会导致系统禁止普通认证登录UNC，网管以普通认证的方式无法登录UNC。

本命令用于设置网管登录 UNC 的认证策略。

## 注意事项

- “认证策略”的系统初始值为“ALL(普通认证和增强认证)”。“ALL(普通认证和增强认证)”采用的认证算法强度较低。“ENHANCED(增强认证)”采用高强度认证算法，建议使用。
- “认证策略”配置为“ENHANCED(增强认证)”时，系统会禁止普通认证登录 UNC ，网管以普通认证的方式无法登录 UNC 。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| AUTHPOL | 认证策略 | 可选必选说明：必选参数。<br>参数含义：指定网管登录<br>UNC<br>的认证策略。<br>取值范围：<br>- “ALL(普通认证和增强认证)”：系统支持网管使用普通认证和增强认证登录<br>UNC<br>。<br>- “ENHANCED(增强认证)”：系统支持网管使用增强认证登录<br>UNC<br>。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTHSOAP]] · 网管登录认证策略（AUTHSOAP）

## 使用实例

设置网管登录认证策略：

```
%%SET AUTHSOAP: AUTHPOL=ALL;%%
RETCODE = 0  操作成功

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置网管登录认证策略（SET-AUTHSOAP）_97634436.md`
