---
id: UNC@20.15.2@MMLCommand@LST SMARTDT
type: MMLCommand
name: LST SMARTDT（查询基于终端类型的DT限制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMARTDT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 基于终端类型的DT限制
status: active
---

# LST SMARTDT（查询基于终端类型的DT限制）

## 功能

**适用网元：SGSN**

此命令用于查询基于终端类型的Direct Tunnel限制的配置。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：可选参数<br>参数含义：待查询的终端类型。<br>取值范围:<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMARTDT]] · 基于终端类型的DT限制（SMARTDT）

## 使用实例

查询基于终端类型的DT限制:

LST SMARTDT: UETYPE=WINDOWS;

```
%%LST SMARTDT: UETYPE=WINDOWS;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
  终端类型  =  Windows
DT限制开关  =  开启
      描述  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMARTDT.md`
