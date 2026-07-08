---
id: UNC@20.15.2@MMLCommand@LST N40DIAGTRIGGER
type: MMLCommand
name: LST N40DIAGTRIGGER（查询N40去活原因的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40DIAGTRIGGER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- N40诊断值Trigger
status: active
---

# LST N40DIAGTRIGGER（查询N40去活原因的映射关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询用户去活时内部诊断字段取值到去活原因的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAGNOSTICS | 诊断原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF内部的去活诊断字段原因值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [N40去活原因的映射关系（N40DIAGTRIGGER）](configobject/UNC/20.15.2/N40DIAGTRIGGER.md)

## 使用实例

查询内部诊断字段取值为259的映射关系：

```
%%LST N40DIAGTRIGGER: DIAGNOSTICS=259;%%
RETCODE = 0  操作成功

结果如下
--------
           诊断原因值  =  259
             去活原因  =  正常去活                
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N40去活原因的映射关系（LST-N40DIAGTRIGGER）_35102634.md`
