---
id: UNC@20.15.2@MMLCommand@LST CGBINDING
type: MMLCommand
name: LST CGBINDING（查询CG绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CGBINDING
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG绑定
status: active
---

# LST CGBINDING（查询CG绑定关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示UNC上已配置的CG组信息。用户可以选择显示指定的CG组信息，也可以显示所有已配置的CG组信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：可选参数<br>参数含义：指定CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：如果不配置则是要查询所有的CG组。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGBINDING]] · CG绑定关系（CGBINDING）

## 使用实例

查询CG绑定关系，命令为：

```
LST CGBINDING:;
```

```

RETCODE = 0  操作成功

CG绑定关系信息
--------------
   CG组ID  =  1
CG IP地址  =  192.168.0.2
 CG端口号  =  25009
     等级  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CGBINDING.md`
