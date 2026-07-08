---
id: UNC@20.15.2@MMLCommand@LST PSAUPFBINDATSSS
type: MMLCommand
name: LST PSAUPFBINDATSSS（查询PSA UPF和ATSSS UPF的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PSAUPFBINDATSSS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- PSA绑定ATSSS
status: active
---

# LST PSAUPFBINDATSSS（查询PSA UPF和ATSSS UPF的绑定关系）

## 功能

**适用NF：SMF**

该命令用于查询PSA UPF和ATSSS UPF绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSAUPFINSTNAME | PSA UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PSA UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”为None的“UPF实例名称”。 |
| ATSSSINSTNAME | ATSSS UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ATSSS UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”取值为ATSSS的“UPF实例名称”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSAUPFBINDATSSS]] · PSA UPF和ATSSS UPF绑定关系中的ATSSS-UPF（PSAUPFBINDATSSS）

## 使用实例

查询PSA UPF和ATSSS UPF的绑定关系：

```
LST PSAUPFBINDATSSS:;
%%LST PSAUPFBINDATSSS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
PSA UPF 实例名称       ATSSS UPF 实例名称  

upf_instance_1         upf_instance_2       
upf_none               upf_atsss_1          
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PSAUPFBINDATSSS.md`
