---
id: UNC@20.15.2@MMLCommand@LST IPV6PREFIXFILTERNODE
type: MMLCommand
name: LST IPV6PREFIXFILTERNODE（查询IPv6前缀过滤器节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6PREFIXFILTERNODE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- IPv6前缀过滤器节点
status: active
---

# LST IPV6PREFIXFILTERNODE（查询IPv6前缀过滤器节点）

## 功能

该命令用于查询基于IPv6信息的前缀过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IPv6前缀列表名字 | 可选必选说明：可选参数<br>参数含义：IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6PREFIXFILTERNODE]] · IPv6前缀过滤器节点（IPV6PREFIXFILTERNODE）

## 使用实例

查询IPv6前缀过滤器：

```
LST IPV6PREFIXFILTERNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
IPv6前缀列表名字    IPv6前缀列表节点号        IPv6前缀列表匹配模式      IPv6地址           前缀长度      是否匹配网络地址       前缀长度匹配范围下限       前缀长度匹配范围上限
one                 1                         允许                      2001:DB8::1        128           FALSE                  NULL                       NULL
two                 1                         允许                      2001:DB8::2        128           FALSE                  128                        128
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPV6PREFIXFILTERNODE.md`
