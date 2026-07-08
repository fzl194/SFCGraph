---
id: UNC@20.15.2@MMLCommand@LST UPFBINDGRP
type: MMLCommand
name: LST UPFBINDGRP（查询UPF和UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFBINDGRP
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
- UE地址管理
- UE地址池管理
- 地址分配UPF组管理
status: active
---

# LST UPFBINDGRP（查询UPF和UPF组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询UPF和UPF组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该参数使用ADD UPNODE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFBINDGRP]] · UPF和UPF组的绑定关系（UPFBINDGRP）

## 使用实例

查询UPF和UPF组的绑定关系：

```
%%LST UPFBINDGRP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     UPF组名称  =  upfgrp1
   UPF实例标识  =  upf_instance_1
        优先级  =  255
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF和UPF组的绑定关系（LST-UPFBINDGRP）_32232822.md`
