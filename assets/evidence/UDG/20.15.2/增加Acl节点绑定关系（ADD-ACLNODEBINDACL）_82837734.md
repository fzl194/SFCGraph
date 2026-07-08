# 增加Acl节点绑定关系（ADD ACLNODEBINDACL）

- [命令功能](#ZH-CN_CONCEPT_0182837734__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837734__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837734__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837734__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837734__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837734)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加ACL节点和ACL的绑定关系。

基于APN做ACL业务控制的场景，需要将ACL节点绑定到ACL下，再将ACL绑定到APN下。这样用户接入在该APN下时，就可以使用ACL节点下配置的策略进行业务控制。

#### [注意事项](#ZH-CN_CONCEPT_0182837734)

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 每条ACL下可以绑定5000条ACL节点。系统整机支持最大的绑定规格是10000。
- 对于ACL为自动排序方式的，在绑定ACL节点时不需要指定优先级，如果指定了优先级，优先级也是无效的。
- ACL正在被使用时，可以继续往ACL上绑定ACL节点。
- ACL节点的动作类型需要与ACL下其他ACL节点的动作类型一致。
- 修改或删除ACL后需要执行SET REFRESHSRV使当前配置生效，建议该操作在对所有ACL的配置修改完成后执行。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837734)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837734)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：参数已通过ADD ACL命令配置，无需重新配置。 |
| ACLNODENAME | ACL节点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：参数已通过ADD ACLNODE命令配置，无需重新配置。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL节点的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：<br>- 该参数的值越小优先级越高。<br>- 当ACL的MatchOrder配置方式为CONFIG时必须要配置优先级。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837734)

- 假如运营商需要在增加一个ACL节点绑定关系到ACL“testacl1”上，ACL为自动排序方式：
  ```
  ADD ACLNODEBINDACL: ACLNAME="testacl1",ACLNODENAME="testaclnode1";
  ```
- 假如运营商需要在增加一个ACL节点绑定关系到ACL“testacl2”上，ACL为优先级排序方式，优先级为25：
  ```
  ADD ACLNODEBINDACL: ACLNAME="testacl2",ACLNODENAME="testaclnode2",PRIORITY=25;
  ```
