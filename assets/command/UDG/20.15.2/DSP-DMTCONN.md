---
id: UDG@20.15.2@MMLCommand@DSP DMTCONN
type: MMLCommand
name: DSP DMTCONN（显示Diameter基本信息或Peer连接相关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DMTCONN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- Diameter基本信息或Peer连接信息
status: active
---

# DSP DMTCONN（显示Diameter基本信息或Peer连接相关信息）

## 功能

该命令用于显示Diameter基本信息或Peer连接相关信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| LOCALORPEER | 是否查询Peer连接信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否查询Peer连接信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Local：本地连接信息。<br>- Peer：远端连接信息。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DMTCONN]] · Diameter基本信息或Peer连接相关信息（DMTCONN）

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DMTCONN.md`
