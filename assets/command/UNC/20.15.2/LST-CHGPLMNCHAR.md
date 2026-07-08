---
id: UNC@20.15.2@MMLCommand@LST CHGPLMNCHAR
type: MMLCommand
name: LST CHGPLMNCHAR（查询PLMN的计费属性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGPLMNCHAR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN计费属性参数配置
status: active
---

# LST CHGPLMNCHAR（查询PLMN的计费属性参数）

## 功能

**适用网元：SGSN**

该命令用于查询PLMN类型的用户计费属性参数的配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMN | PLMN 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于运营商对不同PLMN用户的话单生成采取不同的策略。<br>取值范围：<br>- “HPLMN（本地 PLMN）”：表示本网用户。<br>- “VPLMN（拜访 PLMN）”：表示拜访用户，非本网用户即拜访用户 。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGPLMNCHAR]] · PLMN的计费属性参数（CHGPLMNCHAR）

## 使用实例

查询普通计费属性的配置信息：

LST CHGPLMNCHAR: PLMN=HPLMN;

```
%%LST CHGPLMNCHAR: PLMN=HPLMN;%%
RETCODE = 0  操作成功。

输出结果如下
------------
     PLMN 类型  =  本地 PLMN
     生成M-CDR  =  生成
     生成S-CDR  =  生成
 生成S-SMO-CDR  =  生成
 生成S-SMT-CDR  =  生成
生成LCS-MO-CDR  =  生成
生成LCS-MT-CDR  =  生成
生成LCS-NI-CDR  =  生成
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PLMN的计费属性参数(LST-CHGPLMNCHAR)_72344991.md`
