---
id: UNC@20.15.2@MMLCommand@LST NGTALISTPAGINGCFG
type: MMLCommand
name: LST NGTALISTPAGINGCFG（查询N2模式TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTALISTPAGINGCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG TALIST寻呼管理
status: active
---

# LST NGTALISTPAGINGCFG（查询N2模式TALIST寻呼不重发TAC区间）

## 功能

**适用NF：AMF**

该命令用于查询N2模式TALIST寻呼不重发TAC区间。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| TACSTART | 跟踪区域起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域起始编码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：<br>本参数由6位十六进制数组成，不区分大小写。MCC、MNC相同时，不同记录的TAC区间不能有交集。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGTALISTPAGINGCFG]] · N2模式TALIST寻呼不重发TAC区间（NGTALISTPAGINGCFG）

## 使用实例

查询TALIST寻呼不重发TAC区间，执行如下命令：

```
%%LST NGTALISTPAGINGCFG:;%%
RETCODE = 0  操作成功

结果如下
------------
           MCC  =  123
           MNC  =  45
跟踪区域起始值  =  11BF85
跟踪区域结束值  =  11BF86
   语音寻呼开关 =  否
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N2模式TALIST寻呼不重发TAC区间（LST-NGTALISTPAGINGCFG）_61627198.md`
