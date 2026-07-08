# 转换vHA ETCD集群中节点间通讯地址的方式（STR VHACHGPEER）

- [命令功能](#ZH-CN_MMLREF_0251852643__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0251852643__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0251852643__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0251852643__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0251852643)

![](转换vHA ETCD集群中节点间通讯地址的方式（STR VHACHGPEER）_51852643.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

此命令用于转换vHA ETCD集群中节点间通讯地址的方式。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0251852643)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0251852643)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHANGETYPE | 改变类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示改变类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTODOMAINNAME（IP地址转换为域名方式）<br>- DOMAINNAMETOIP（域名方式转换为IP地址）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0251852643)

- 将vHA ETCD集群中节点通讯地址从IP地址转换为域名方式。
  ```
  STR VHACHGPEER: CHANGETYPE=IPTODOMAINNAME;
  ```
- 将vHA ETCD集群中节点通讯地址从域名方式转换为IP地址。
  ```
  STR VHACHGPEER: CHANGETYPE=DOMAINNAMETOIP;
  ```
