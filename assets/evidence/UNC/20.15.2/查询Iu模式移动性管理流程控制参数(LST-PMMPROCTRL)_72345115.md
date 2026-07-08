# 查询Iu模式移动性管理流程控制参数(LST PMMPROCTRL)

- [命令功能](#ZH-CN_MMLREF_0000001172345115__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345115__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345115__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345115__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345115__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345115__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172345115__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345115)

**适用网元：SGSN**

此命令用于查询Iu模式移动性管理流程控制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001172345115)

- 此命令执行后立即生效。
- 若不输入流程类型，则将显示所有流程类型的原因值。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345115)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345115)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345115)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：待查询的流程类型。<br>取值范围：<br>- “ATTACH(附着流程)”<br>- “INTER_RAU(USN间路由区域更新流程)”<br>- “INTRA_RAU(USN内路由区域更新流程)”<br>- “UPDATE_LOCATION(位置更新流程)”<br>- “IU_RELEASE(Iu连接释放流程)”<br>- “AIR(获取鉴权集流程)”<br>- “AUTHENTICATION(鉴权流程)”<br>- “CHECK_IMEI(检查IMEI流程)”<br>- “PAGING(寻呼流程)”<br>- “CANCEL_LOCATION(位置取消流程)”<br>- “NET_SHARE(网络共享)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345115)

查询流程类型为UPDATE_LOCATION（位置更新流程）的Iu模式移动性管理流程控制参数：

LST PMMPROCTRL: PROT=UPDATE_LOCATION;

```
%%LST PMMPROCTRL: PROT=UPDATE_LOCATION;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                    ULR拒绝原因值（IMSIGT错误）=  0
                    ULR拒绝原因值（SCCPGT错误）=  0
                      ULR拒绝原因值（链路异常）=  0
                   ULR拒绝原因值（HLR/HSS超时）=  0
                   ULR拒绝原因值（HLR/HSS拒绝）=  0
        ULR拒绝原因值（Diagnose为IMSI Unknown）=  0
ULR拒绝原因值（Diagnose为Subscription Unknown）=  0
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172345115)

参见 [**SET PMMPROCTRL**](设置Iu模式移动性管理流程控制参数（SET PMMPROCTRL）_26305328.md) 的参数说明。
