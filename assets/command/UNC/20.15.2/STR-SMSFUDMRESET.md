---
id: UNC@20.15.2@MMLCommand@STR SMSFUDMRESET
type: MMLCommand
name: STR SMSFUDMRESET（启动SMSF的UDM重选）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: SMSFUDMRESET
command_category: 动作类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM重选管理
status: active
---

# STR SMSFUDMRESET（启动SMSF的UDM重选）

## 功能

**适用NF：SMSF**

该命令用于启动SMSF的UDM重选。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDMINSTANCEID | UDM的InstanceID | 可选必选说明：必选参数<br>参数含义：该参数表示用户当前注册的UDM InstanceId。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMSF的UDM重选（SMSFUDMRESET）](configobject/UNC/20.15.2/SMSFUDMRESET.md)

## 使用实例

当运营商希望手动启动UDM的扫描重选，执行如下命令：

```
（1）在SMSF上执行LST NFUUID查询到UDM的InstanceID。
LST NFUUID:;
%%LST NFUUID:;%%
RETCODE = 0  操作成功

结果如下
--------
    NF类型  =  NfUDM
NF实例名称  =  UDM_Instance_28
NF实例标识  =  2a22b585-995d-4b84-78b2-c389920f952b

(结果个数 = 1)

---    END

（2）指定该UDM上的用户重新注册到其它可用的UDM上。
STR SMSFUDMRESET: UDMINSTANCEID="2a22b585-995d-4b84-78b2-c389920f952b";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动SMSF的UDM重选（STR-SMSFUDMRESET）_46413383.md`
