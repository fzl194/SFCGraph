---
id: UNC@20.15.2@MMLCommand@LST HTTPESCAPE
type: MMLCommand
name: LST HTTPESCAPE（查询HTTP对于URL转义的参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPESCAPE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP属性管理
status: active
---

# LST HTTPESCAPE（查询HTTP对于URL转义的参数）

## 功能

该命令用于查询HTTP对于URL转义的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPESCAPE]] · HTTP对于URL转义的参数（HTTPESCAPE）

## 使用实例

如果想查询HTTP转义参数，可以用如下命令：

```
%%LST HTTPESCAPE:;%%
RETCODE = 0  操作成功

结果如下
--------
      URL中加号解码成空格开关  =  关闭
丢弃URL中存在特殊字符消息开关  =  开启
     URL中Json类型参数编码开关 =  关闭
     服务端对URL进行解码的时机 =  解析组件前
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPESCAPE.md`
