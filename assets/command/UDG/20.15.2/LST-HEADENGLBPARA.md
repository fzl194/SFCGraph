---
id: UDG@20.15.2@MMLCommand@LST HEADENGLBPARA
type: MMLCommand
name: LST HEADENGLBPARA（查询头增强全局参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HEADENGLBPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强公共参数
status: active
---

# LST HEADENGLBPARA（查询头增强全局参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询头增强全局参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/HEADENGLBPARA]] · 头增强全局参数（HEADENGLBPARA）

## 使用实例

假如运营商需要查询头增强全局参数：

```
LST HEADENGLBPARA:;
```

```

RETCODE = 0  操作成功。

头增强全局参数信息
------------------
        MSISDN字段最小长度  =  1
 RSA加密节点老化时间（分）  =  10
           RSA证书过期告警  =  使能
   RSA证书过期告警提前天数  =  30
头增强插入盐值生成方法类型  =  随机数
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询头增强全局参数（LST-HEADENGLBPARA）_82837514.md`
