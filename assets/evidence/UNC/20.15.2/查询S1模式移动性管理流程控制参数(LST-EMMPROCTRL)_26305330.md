# 查询S1模式移动性管理流程控制参数(LST EMMPROCTRL)

- [命令功能](#ZH-CN_MMLREF_0000001126305330__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305330__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305330__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305330__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305330__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305330__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305330__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305330)

**适用网元：MME**

此命令用于查询S1模式移动性管理流程控制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001126305330)

- 此命令执行后立即生效。
- 若不输入流程类型，则将显示所有流程类型的原因值。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305330)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305330)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305330)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：待查询的流程类型。<br>取值范围：<br>- “ATTACH(附着流程)”<br>- “INTER_TAU(USN间跟踪区域更新流程)”<br>- “UPDATE_LOCATION(更新位置流程)”<br>- “AIR(获取鉴权集流程)”<br>- “AUTHENTICATION(鉴权流程)”<br>- “CHECK_IMEI(检查IMEI流程)”<br>- “PAGING(寻呼流程)”<br>- “LOCATION_UPDATE(位置更新流程)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305330)

查询 “流程类型” 为 “UPDATE_LOCATION（位置更新流程）” 的S1模式移动性管理流程控制参数：

LST EMMPROCTRL: PROT=UPDATE_LOCATION;

```
%%LST EMMPROCTRL: PROT=UPDATE_LOCATION;%%
RETCODE = 0  操作成功

查询结果如下
--------------
                          ULR拒绝原因值（HSS超时）  =  10
                          ULR拒绝原因值（HSS拒绝）  =  10
                 ULR拒绝原因值（Diameter链路异常）  =  10
                      ULR拒绝原因值（S6a接口流控）  =  10
  ULR拒绝原因值（未知EPS签约用户，有GPRS签约数据）  =  10
ULR拒绝原因值（未知EPS签约用户，没有GPRS签约数据）  =  10
                          ULR拒绝原因值（ODB限制）  =  10
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305330)

参见 [**SET EMMPROCTRL**](设置S1模式移动性管理流程控制参数(SET EMMPROCTRL)_72225199.md) 的参数说明。
