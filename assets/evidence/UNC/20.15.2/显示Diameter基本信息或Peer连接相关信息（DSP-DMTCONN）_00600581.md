# 显示Diameter基本信息或Peer连接相关信息（DSP DMTCONN）

- [命令功能](#ZH-CN_CONCEPT_0000001600600581__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600600581__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600600581__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600600581__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600600581__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600600581__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600600581)

该命令用于显示Diameter基本信息或Peer连接相关信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600600581)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600600581)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600600581)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| LOCALORPEER | 是否查询Peer连接信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否查询Peer连接信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Local：本地连接信息。<br>- Peer：远端连接信息。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600600581)

- 显示Peer连接相关信息：
  ```
  DSP DMTCONN:RUNAME="VNODE_VNRS_VNFC_OMU_0001",LOCALORPEER=Peer;
  ```
  ```

  RETCODE = 0  操作成功。

  Peer信息如下
  ------------
      Peer地址  =  192.168.1.3
        连接ID  =  1
      Peer状态  =  Up
  Peer连接时长  =  255
      本端端口  =  3868
      Peer端口  =  64951
       Peer ID  =  1
      连接组ID  =  1
  (结果个数 = 1)
  ---    END
  ```
- 显示Local连接相关信息：
  ```
  DSP DMTCONN:RUNAME="VNODE_VNRS_VNFC_OMU_0001",LOCALORPEER=Local;
  ```
  ```

  RETCODE = 0  操作成功。

  本地信息如下
  ------------
  Diameter角色  =  Server
      本端地址  =  192.168.1.1
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600600581)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Diameter角色 | 用于表示Diameter角色。 |
| 本端地址 | 用于表示本端IP地址。 |
| Peer地址 | 用于表示Peer IP地址。 |
| 连接ID | 用于表示连接ID。 |
| Peer状态 | 用于表示Peer状态。 |
| Peer连接时长 | 用于表示Peer连接时长。 |
| 本端端口 | 用于表示本端端口。 |
| Peer端口 | 用于表示Peer端口。 |
| Peer ID | 用于表示Peer ID。 |
| 连接组ID | 用于表示连接组ID。 |
