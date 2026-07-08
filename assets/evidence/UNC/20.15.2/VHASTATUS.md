# 更改vHA ETCD节点进程状态（CHG VHASTATUS）

- [命令功能](#ZH-CN_MMLREF_0251852641__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0251852641__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0251852641__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0251852641__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0251852641)

![](更改vHA ETCD节点进程状态（CHG VHASTATUS）_51852641.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致业务故障无法恢复，请谨慎使用并联系华为技术支持协助操作。

此命令用于挂起、重启或清除DB数据后重启所有vHA ETCD集群中ETCD节点进程。

## [注意事项](#ZH-CN_MMLREF_0251852641)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0251852641)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0251852641)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示操作类型。<br>数据来源：本端规划<br>取值范围：<br>- SUSPEND（挂起）<br>- RESTART（重启）<br>- INITIAL（清空数据启动）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0251852641)

- 将vHA ETCD集群中ETCD节点进程挂起。
  ```
  CHG VHASTATUS: ACTION=SUSPEND;
  ```
- 将vHA ETCD集群中ETCD节点进程重启。
  ```
  CHG VHASTATUS: ACTION=RESTART;
  ```
- 将vHA ETCD集群中ETCD节点进程清空DB数据后重启。
  ```
  CHG VHASTATUS: ACTION=INITIAL;
  ```
