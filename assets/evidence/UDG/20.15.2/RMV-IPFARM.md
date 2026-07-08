# 删除IPFarm（RMV IPFARM）

- [命令功能](#ZH-CN_CONCEPT_0182837052__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837052__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837052__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837052__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837052__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837052)

**适用NF：PGW-U、UPF**

![](删除IPFarm（RMV IPFARM）_82837052.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除IP farm可能导致业务无法访问。

该命令用于删除一个IP farm，同时批量删除该IP farm下的所有IP farm服务器。

#### [注意事项](#ZH-CN_CONCEPT_0182837052)

- 该命令执行后立即生效。
- 如果规则中配置的CaptivePortal智能重定向引用了该IP farm，或者有PcscfGroup已经绑定该IP farm对应的Virtual IP，可能会导致该IP farm对应用户当前的重定向业务中断，或者导致p-cscf连接状态检测机制失效，则不允许删除该IP farm。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837052)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837052)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837052)

假设需要删除一个名称为test的IP Farm，则使用如下命令：

```
RMV IPFARM:IPFARMNAME="test";
```
