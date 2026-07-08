---
id: UDG@20.15.2@MMLCommand@LST AIFUNCPARA
type: MMLCommand
name: LST AIFUNCPARA（显示SA Intelligence功能参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AIFUNCPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- Intelligence SA模式数据库
- SA Intelligence功能开关
status: active
---

# LST AIFUNCPARA（显示SA Intelligence功能参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询SA intelligence功能参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SA Intelligence功能参数（AIFUNCPARA）](configobject/UDG/20.15.2/AIFUNCPARA.md)

## 使用实例

假如运营商需要查询SA intelligence功能参数：

```
LST AIFUNCPARA:;
```

```

RETCODE = 0  操作成功

SA Intelligence功能参数
-----------------------
   SA Intelligence功能开关  =  不使能（关闭）
Intelligence验证流的抽样率  =  0
      Intelligence验证流数  =  2000
Intelligence验证流的有效率  =  9900
        SA协议解析加速开关  =  使能（开启）
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SA-Intelligence功能参数（LST-AIFUNCPARA）_93749057.md`
