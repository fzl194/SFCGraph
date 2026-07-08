---
id: UNC@20.15.2@MMLCommand@DSP NGTANEIBS
type: MMLCommand
name: DSP NGTANEIBS（显示TA邻接关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGTANEIBS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- TA邻接关系管理
status: active
---

# DSP NGTANEIBS（显示TA邻接关系）

## 功能

**适用NF：AMF**

查询指定TA的邻接TA列表，对系统无影响。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | TA标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定中心跟踪区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位十进制数字，MNC为2位或者3位十进制数字，填写时请遵循实际长度。TAC编码为十六进制数，长度固定为6位；若不足则左起用0补足6位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGTANEIBS]] · TA邻接关系（NGTANEIBS）

## 使用实例

查询标识为46001000101的中心TA的邻接TA列表，执行如下命令：

```
%%DSP NGTANEIBS:TAI="46001000101";%%
RETCODE = 0  操作成功

结果如下
--------

邻接TA标识  =  46001000102
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示TA邻接关系（DSP-NGTANEIBS）_76181741.md`
