# 启动SMSF的UDM重选（STR SMSFUDMRESET）

- [命令功能](#ZH-CN_MMLREF_0000001146413383__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001146413383__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001146413383__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001146413383__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001146413383)

**适用NF：SMSF**

该命令用于启动SMSF的UDM重选。

## [注意事项](#ZH-CN_MMLREF_0000001146413383)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001146413383)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001146413383)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDMINSTANCEID | UDM的InstanceID | 可选必选说明：必选参数<br>参数含义：该参数表示用户当前注册的UDM InstanceId。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001146413383)

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
