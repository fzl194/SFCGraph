---
id: UNC@20.15.2@MMLCommand@LST NDGLOBALCONFIG
type: MMLCommand
name: LST NDGLOBALCONFIG（查询IPv6 ND系统配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NDGLOBALCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND全局配置
status: active
---

# LST NDGLOBALCONFIG（查询IPv6 ND系统配置）

## 功能

该命令用于查询IPv6 ND全局配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NDGLOBALCONFIG]] · IPv6 ND系统配置（NDGLOBALCONFIG）

## 使用实例

查询IPv6 ND全局配置：

```
LST NDGLOBALCONFIG:;
```

```

RETCODE = 0   操作成功

结果如下
------------------------
     使能预探测  =  关闭
   使能自动探测  =  开启
           跳限  =  101
       速率限制  =  0
  失效时间（s）  =  1200
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NDGLOBALCONFIG.md`
