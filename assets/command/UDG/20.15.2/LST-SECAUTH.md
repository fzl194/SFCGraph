---
id: UDG@20.15.2@MMLCommand@LST SECAUTH
type: MMLCommand
name: LST SECAUTH（查看二次授权功能状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECAUTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 二次授权状态管理
status: active
---

# LST SECAUTH（查看二次授权功能状态）

## 功能

查询二次授权功能状态，显示二次授权功能是否开启。

## 注意事项

如果25.0.0之前版本开启二次授权功能，升级到25.0.0及之后版本， “是否打开免二次授权时间段” 、 “开始日期” 、 “结束日期” 、 “开始时间” 及 “结束时间” 参数默认为NULL。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECAUTH]] · 查看二次授权功能状态（SECAUTH）

## 使用实例

查询二次授权功能状态：

```
%%LST SECAUTH:;%%
RETCODE = 0  操作成功

操作结果如下
------------
              二次授权状态  =  开启二次授权功能
  是否打开免二次授权时间段  =  否
                  开始日期  =  NULL
                  结束日期  =  NULL
                  开始时间  =  NULL
                  结束时间  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SECAUTH.md`
