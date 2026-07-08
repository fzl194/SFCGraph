---
id: UDG@20.15.2@MMLCommand@LST SECAUTHMEM
type: MMLCommand
name: LST SECAUTHMEM（查看二次授权命令）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECAUTHMEM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 二次授权命令管理
status: active
---

# LST SECAUTHMEM（查看二次授权命令）

## 功能

查询需要二次授权的命令列表。

## 注意事项

网元ID必须在系统中存在。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：网元ID。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |
| COMMAND | 命令名称 | 可选必选说明：可选参数<br>参数含义：需要查询的MML命令名称。<br>取值范围：长度不超过80的英文字符串。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [二次授权命令（SECAUTHMEM）](configobject/UDG/20.15.2/SECAUTHMEM.md)

## 使用实例

查看二次授权命令：

```
%%LST SECAUTHMEM:;%%
RETCODE = 0  操作成功

操作结果如下
------------
网元ID  命令名称     提示信息  

0       LST CONNECT  NULL              
0       LST WKSP     NULL         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看二次授权命令（LST-SECAUTHMEM）_88107917.md`
