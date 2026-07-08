---
id: UNC@20.15.2@MMLCommand@LST PERFREGTAC
type: MMLCommand
name: LST PERFREGTAC（查询区域性能统计对象和TAC段的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFREGTAC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFREGTAC（查询区域性能统计对象和TAC段的绑定关系）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来查询区域性能统计对象和TAC段的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REGNAME | 区域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定与TAC段绑定的区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACSEGNAME | TAC段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定与区域绑定的TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [区域性能统计对象和TAC段的绑定关系（PERFREGTAC）](configobject/UNC/20.15.2/PERFREGTAC.md)

## 使用实例

当运营商需要查询一个区域性能统计对象关联的TAC号段时，执行如下命令：

```
LST PERFREGTAC: REGNAME="beijing", TACSEGNAME="changping";
%%LST PERFREGTAC: REGNAME="beijing", TACSEGNAME="changping";%%
RETCODE = 0  操作成功

结果如下
--------
 区域名称  =  beijing
TAC段名称  =  changping
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询区域性能统计对象和TAC段的绑定关系（LST-PERFREGTAC）_44529806.md`
