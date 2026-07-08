---
id: UNC@20.15.2@MMLCommand@LST CPNODE
type: MMLCommand
name: LST CPNODE（查询CP节点信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPNODE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- CP管理
- CP节点管理
status: active
---

# LST CPNODE（查询CP节点信息）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询CP节点信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNODEINDEX | CP节点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CP节点索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPNODE]] · CP节点信息（CPNODE）

## 使用实例

- 查询有的CP节点： LST CPNODE:;
  ```
  %%LST CPNODE:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
      CP节点索引  =  0
    CP节点ID类型  =  IPV4
  CP节点IPv4地址  =  192.168.0.10
  CP节点FQDN域名  =  NULL
      CP节点功能  =  0
  (结果个数 = 1)
  ```
- 查询CP节点索引为0的CP节点： LST CPNODE: CPNODEINDEX=0;
  ```
  %%LST CPNODE: CPNODEINDEX=0;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
      CP节点索引  =  0
    CP节点ID类型  =  IPV4
  CP节点IPv4地址  =  192.168.0.10
  CP节点FQDN域名  =  NULL
      CP节点功能  =  0
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CPNODE.md`
