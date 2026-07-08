---
id: UNC@20.15.2@MMLCommand@LST INTELLISUFFIX
type: MMLCommand
name: LST INTELLISUFFIX（查询智能业务后缀）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTELLISUFFIX
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 智能业务后缀
status: active
---

# LST INTELLISUFFIX（查询智能业务后缀）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询智能业务后缀。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTELLISUFFIX | 智能业务后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于设置智能业务后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [智能业务后缀（INTELLISUFFIX）](configobject/UNC/20.15.2/INTELLISUFFIX.md)

## 使用实例

查询“增加智能业务后缀”为“intelligent”的INTELLISUFFIX配置：

```
%%LST INTELLISUFFIX: INTELLISUFFIX="intelligent";%%
RETCODE = 0  操作成功

结果如下
------------------------
                智能业务后缀  =  intelligent
                智能业务名称  =  video
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询智能业务后缀（LST-INTELLISUFFIX）_22697900.md`
