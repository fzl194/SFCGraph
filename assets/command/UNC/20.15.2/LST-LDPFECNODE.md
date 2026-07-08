---
id: UNC@20.15.2@MMLCommand@LST LDPFECNODE
type: MMLCommand
name: LST LDPFECNODE（查询FEC节点配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LDPFECNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC节点
status: active
---

# LST LDPFECNODE（查询FEC节点配置）

## 功能

该命令用于查询FEC节点配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FEC的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPFECNODE]] · FEC节点（LDPFECNODE）

## 使用实例

查询FEC节点配置：

```
LST LDPFECNODE:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
FEC列表名称  =  name1
     IP地址  =  192.168.1.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LDPFECNODE.md`
