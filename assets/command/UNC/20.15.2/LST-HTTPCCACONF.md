---
id: UNC@20.15.2@MMLCommand@LST HTTPCCACONF
type: MMLCommand
name: LST HTTPCCACONF（查询HTTP CCA属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPCCACONF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP CCA安全管理
status: active
---

# LST HTTPCCACONF（查询HTTP CCA属性）

## 功能

该命令用于查询HTTP CCA属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [HTTP CCA属性（HTTPCCACONF）](configobject/UNC/20.15.2/HTTPCCACONF.md)

## 使用实例

如果想查询HTTP CCA属性，可以用如下命令：

```
%%LST HTTPCCACONF:;%%
RETCODE = 0  操作成功

结果如下
--------
     CCA校验开关  =  打开
CCA的有效时长(s)  =  86400
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP-CCA属性（LST-HTTPCCACONF）_54738721.md`
