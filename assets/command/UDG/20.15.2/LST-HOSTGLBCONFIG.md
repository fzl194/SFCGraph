---
id: UDG@20.15.2@MMLCommand@LST HOSTGLBCONFIG
type: MMLCommand
name: LST HOSTGLBCONFIG（查询主机收发全局属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HOSTGLBCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP协议全局配置
status: active
---

# LST HOSTGLBCONFIG（查询主机收发全局属性）

## 功能

该命令用于查询主机收发忽略管理平面接口上送的TCP或UDP协议报文的校验和。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HOSTGLBCONFIG]] · 主机收发全局属性（HOSTGLBCONFIG）

## 使用实例

查询主机收发忽略校验和：

```
LST HOSTGLBCONFIG:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
          忽略校验和  = TRUE
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HOSTGLBCONFIG.md`
