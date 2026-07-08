---
id: UNC@20.15.2@MMLCommand@LST CPCGBINDING
type: MMLCommand
name: LST CPCGBINDING（显示抄送CG绑定）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPCGBINDING
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
- 抄送CG绑定
status: active
---

# LST CPCGBINDING（显示抄送CG绑定）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示UNC上已配置的抄送CG组信息。用户可以选择显示指定的抄送CG组信息，也可以显示所有已配置的抄送CG组信息。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPCGGRPID | 抄送CG组ID | 可选必选说明：可选参数<br>参数含义：指定抄送CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。整数1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPCGBINDING]] · 抄送CG绑定关系（CPCGBINDING）

## 使用实例

查询抄送CG绑定关系，命令为：

```
LST CPCGBINDING:;
```

```

RETCODE = 0  操作成功

抄送CG绑定
----------
抄送CG组ID  =  1
 CG IP地址  =  192.168.0.2
  CG端口号  =  25009
      等级  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CPCGBINDING.md`
