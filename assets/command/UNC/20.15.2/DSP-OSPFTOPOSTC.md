---
id: UNC@20.15.2@MMLCommand@DSP OSPFTOPOSTC
type: MMLCommand
name: DSP OSPFTOPOSTC（查询OSPF拓扑的统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFTOPOSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF拓扑统计信息
status: active
---

# DSP OSPFTOPOSTC（查询OSPF拓扑的统计信息）

## 功能

该命令用于查询OSPF拓扑的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示OSPF进程号，未指定OSPF进程号时默认查询所有OSPF进程。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFTOPOSTC]] · OSPF拓扑的统计信息（OSPFTOPOSTC）

## 使用实例

查询OSPF拓扑的统计信息：

```
DSP OSPFTOPOSTC:PROCID=2;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
               OSPF进程号  =  2
               OSPF区域号  =  10.10.10.10
               路由器标识  =  192.168.3.3
              SPT节点总数  =  3
        SPT路由器节点数量  =  2
      SPT网络类型节点数量  =  1
    参与SPT计算的节点数量  =  3
           隔离的节点数量  =  0
SPT计算最大距离的节点数量  =  1
                 Link数量  =  4
 父节点到子节点的Link数量  =  2
 子节点到父节点的Link数量  =  2
                  SPF状态  =  已完成
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFTOPOSTC.md`
