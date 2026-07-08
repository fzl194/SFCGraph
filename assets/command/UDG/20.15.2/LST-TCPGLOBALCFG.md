---
id: UDG@20.15.2@MMLCommand@LST TCPGLOBALCFG
type: MMLCommand
name: LST TCPGLOBALCFG（查询TCP全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TCPGLOBALCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- TCP全局配置
status: active
---

# LST TCPGLOBALCFG（查询TCP全局配置）

## 功能

该命令用于查询TCP全局配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPGLOBALCFG]] · TCP全局配置（TCPGLOBALCFG）

## 使用实例

查询TCP全局配置：

```
LST TCPGLOBALCFG:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        TCP FIN-Wait超时时间（s）  =  675
        TCP SYN-Wait超时时间（s）  =  75
                  TCP窗口值（KB）  =  8
                     PMTU功能开关  =  打开
              PMTU老化时间（min）  =  100
   IPv6 TCP FIN-Wait超时时间（s）  =  675
   IPv6 TCP SYN-Wait超时时间（s）  =  75
             IPv6 TCP窗口值（KB）  =  8
                最大MSS值（byte）  =  65535
            IPv6最大MSS值（byte）  =  65535
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP全局配置（LST-TCPGLOBALCFG）_00601361.md`
