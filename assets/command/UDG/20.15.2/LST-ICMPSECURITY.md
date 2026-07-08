---
id: UDG@20.15.2@MMLCommand@LST ICMPSECURITY
type: MMLCommand
name: LST ICMPSECURITY（查询ICMP安全配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ICMPSECURITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- ICMP安全配置
status: active
---

# LST ICMPSECURITY（查询ICMP安全配置）

## 功能

该命令用于查询ICMP安全配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICMPSECURITY]] · ICMP安全配置（ICMPSECURITY）

## 使用实例

查询系统ICMP安全配置实例：

```
LST ICMPSECURITY:;
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
            报文方向  =  接收报文
        ICMP配置类型  =  报文类型
        ICMP报文类型  =  回显请求：Type=8, Code=0
                类型  =  8
                编码  =  0
        ICMP配置开关  =  使能
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ICMP安全配置（LST-ICMPSECURITY）_00600705.md`
