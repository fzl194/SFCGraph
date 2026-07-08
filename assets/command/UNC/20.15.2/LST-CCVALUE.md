---
id: UNC@20.15.2@MMLCommand@LST CCVALUE
type: MMLCommand
name: LST CCVALUE（查询计费特征值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCVALUE
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 计费特征值
status: active
---

# LST CCVALUE（查询计费特征值）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于查询计费属性组下绑定的计费特征值信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCGROUPNAME | 计费特征组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费特征组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。由英文字母（大小写）、数字、下划线构成的字符串，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD CCGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCVALUE]] · 计费特征值（CCVALUE）

## 使用实例

查询“计费特征组名称”为“c1”的计费特征值配置：

```
%%LST CCVALUE: CCGROUPNAME="c1";%%
RETCODE = 0  操作成功

结果如下
------------------------
计费特征组名称  计费特征值  

c1              0x0000                         
c1              0x1111                         
c1              0x1234                         
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCVALUE.md`
