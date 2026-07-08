# 设置升级状态（SET UPDSTATUS）

- [命令功能](#ZH-CN_TOPIC_0000001087929894__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000001087929894__1.3.2.1)
- [操作用户权限](#ZH-CN_TOPIC_0000001087929894__1.3.3.1)
- [参数说明](#ZH-CN_TOPIC_0000001087929894__1.3.4.1)
- [使用实例](#ZH-CN_TOPIC_0000001087929894__1.3.5.1)

#### [命令功能](#ZH-CN_TOPIC_0000001087929894)

![](设置升级状态（SET UPDSTATUS）_87929894.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，执行该命令会设置升级状态，某些服务的状态会受到影响。若错误设置某些服务的升级状态，可能会导致该服务升级失败。请谨慎使用。

该命令用于设置RU升级开始和结束。

#### [注意事项](#ZH-CN_TOPIC_0000001087929894)

- 该命令执行后立即生效。
- 如果主主控没有设置升级开始，其他单板不能设置升级开始。

#### [操作用户权限](#ZH-CN_TOPIC_0000001087929894)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000001087929894)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| SETSTATUS | 设置状态 | 可选必选说明：必选参数<br>参数含义：该参数用于设置升级状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- On：开始升级。<br>- Off：结束升级。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

#### [使用实例](#ZH-CN_TOPIC_0000001087929894)

设置RU升级状态：

```
SET UPDSTATUS:SETSTATUS=On,
SERVICEINSTANCE="vnfc"
;
SET UPDSTATUS:SETSTATUS=Off,
SERVICEINSTANCE="vnfc"
;
SET UPDSTATUS:RUNAME="VNODE_UGW_VNFC_OMU_0001",SETSTATUS=On,
SERVICEINSTANCE="vnfc"
;
SET UPDSTATUS:RUNAME="VNODE_UGW_VNFC_SPU_0065",SETSTATUS=Off,
SERVICEINSTANCE="vnfc"
;
```
