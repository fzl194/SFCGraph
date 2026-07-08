---
id: UNC@20.15.2@MMLCommand@LST AMFSBIINFCTRL
type: MMLCommand
name: LST AMFSBIINFCTRL（查询AMF的SBI接口控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFSBIINFCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- AMF服务化接口兼容性参数管理
status: active
---

# LST AMFSBIINFCTRL（查询AMF的SBI接口控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF的SBI接口控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFSBIINFCTRL]] · AMF的SBI接口控制参数（AMFSBIINFCTRL）

## 使用实例

查询AMF的SBI接口控制参数，执行如下命令：

```
%%LST AMFSBIINFCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
            Schema自适应开关  =  关闭
ModelD模式UDM Schema填充策略  =  HTTP优先
ModelD模式PCF Schema填充策略  =  HTTP优先
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF的SBI接口控制参数（LST-AMFSBIINFCTRL）_08368061.md`
