---
id: UNC@20.15.2@MMLCommand@LST PREFIXFILTERNODE
type: MMLCommand
name: LST PREFIXFILTERNODE（查询IPv4地址前缀列表过滤器节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PREFIXFILTERNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- IP前缀列表
status: active
---

# LST PREFIXFILTERNODE（查询IPv4地址前缀列表过滤器节点）

## 功能

该命令用于查询已配置的前缀过滤器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IP前缀列表名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PREFIXFILTERNODE]] · IPv4地址前缀列表过滤器节点（PREFIXFILTERNODE）

## 使用实例

查询前缀过滤器信息：

```
LST PREFIXFILTERNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
    IP前缀列表名字  =  a
  IP前缀列表节点号  =  10
IP前缀列表匹配模式  =  拒绝
            IP地址  =  10.1.1.1
          掩码长度  =  32
        大于或等于  =  NULL
        小于或等于  =  NULL
      是否匹配网络  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv4地址前缀列表过滤器节点（LST-PREFIXFILTERNODE）_00440853.md`
