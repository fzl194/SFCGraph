---
id: UNC@20.15.2@MMLCommand@LST HTTPINFORPT
type: MMLCommand
name: LST HTTPINFORPT（查询HTTP连接信息上报参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPINFORPT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP CHR上报管理
status: active
---

# LST HTTPINFORPT（查询HTTP连接信息上报参数）

## 功能

本命令用于查询HTTP连接信息上报的控制参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPINFORPT]] · HTTP连接信息上报参数（HTTPINFORPT）

## 使用实例

如果想查询HTTP连接信息上报的控制参数，可以用如下命令：

```
%%LST HTTPINFORPT:;%%
RETCODE = 0  操作成功

结果如下
--------
          HTTP连接信息上报列表  =  HTTP动态头压缩字典上报
HTTP动态头域压缩字典上报定时器  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP连接信息上报参数（LST-HTTPINFORPT）_84132100.md`
