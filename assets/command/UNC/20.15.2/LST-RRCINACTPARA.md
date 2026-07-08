---
id: UNC@20.15.2@MMLCommand@LST RRCINACTPARA
type: MMLCommand
name: LST RRCINACTPARA（查询RRC Inactive参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RRCINACTPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- RRC Inactive业务管理
- RRC Inactive参数
status: active
---

# LST RRCINACTPARA（查询RRC Inactive参数）

## 功能

**适用NF：AMF**

该命令用于查询RRC Inactive参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [RRC Inactive参数（RRCINACTPARA）](configobject/UNC/20.15.2/RRCINACTPARA.md)

## 使用实例

查询RRC Inactive参数配置，执行如下命令：

```
%%LST RRCINACTTAI:;%%
RETCODE = 0  操作成功

输出结果如下
--------------
位置获取超时  =  失败响应
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RRC-Inactive参数（LST-RRCINACTPARA）_70462561.md`
