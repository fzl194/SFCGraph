---
id: UNC@20.15.2@MMLCommand@LST ICMPOPTSECURITY
type: MMLCommand
name: LST ICMPOPTSECURITY（查询ICMP选项安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ICMPOPTSECURITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- ICMP选项安全配置
status: active
---

# LST ICMPOPTSECURITY（查询ICMP选项安全配置）

## 功能

该命令用于查询ICMP选项安全配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ICMPOPTSECURITY]] · ICMP选项安全配置（ICMPOPTSECURITY）

## 使用实例

查询ICMP选项安全配置：

```
LST ICMPOPTSECURITY:;
```

```

        RETCODE = 0  操作成功

        结果如下
        ------------------------
              RU名称  =  VNODE_VNRS_VNFC_IPU_0064
        ICMP安全类型  =  TTL超时报文
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ICMPOPTSECURITY.md`
