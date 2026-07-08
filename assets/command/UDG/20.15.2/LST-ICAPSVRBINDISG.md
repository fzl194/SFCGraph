---
id: UDG@20.15.2@MMLCommand@LST ICAPSVRBINDISG
type: MMLCommand
name: LST ICAPSVRBINDISG（查询ICAP服务器绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ICAPSVRBINDISG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器绑定
status: active
---

# LST ICAPSVRBINDISG（查询ICAP服务器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询ICAP Server与ICAP Server Group的绑定关系。如果没有具体指定服务器组的名称，则显示所有已配置的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ICAPSVRBINDISG]] · ICAP服务器绑定关系（ICAPSVRBINDISG）

## 使用实例

查询ICAP Server服务器绑定信息：

```
LST ICAPSVRBINDISG:ICAPSVRGRPNAME="isg1";
```

```

RETCODE = 0  操作成功

ICAP服务器绑定关系信息
----------------------
ICAP服务器组名称  =  isg1
  ICAP服务器名称  =  is1
      配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ICAP服务器绑定关系（LST-ICAPSVRBINDISG）_32260089.md`
