---
id: UNC@20.15.2@MMLCommand@LST ATTACKDEFEND
type: MMLCommand
name: LST ATTACKDEFEND（查询攻击防范参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ATTACKDEFEND
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- 攻击防范
status: active
---

# LST ATTACKDEFEND（查询攻击防范参数）

## 功能

该命令用于查询攻击防范参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [攻击防范参数（ATTACKDEFEND）](configobject/UNC/20.15.2/ATTACKDEFEND.md)

## 使用实例

查询攻击防范配置参数：

```
LST ATTACKDEFEND:;
```

```

        RETCODE = 0  操作成功

        结果如下：
        ------------------------
                 畸形报文使能标志  =  去使能
                  UDP泛洪使能标志  =  去使能
                  TCP-SYN使能标志  =  使能
                 ICMP泛洪使能标志  =  去使能
                 分片报文使能标志  =  使能
           分片报文CIR值（bit/s）  =  89990
           ICMP报文CIR值（bit/s）  =  25666
        TCP-SYN报文CIR值（bit/s）  =  155000000
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询攻击防范参数（LST-ATTACKDEFEND）_49961062.md`
