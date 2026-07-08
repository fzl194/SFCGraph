---
id: UNC@20.15.2@MMLCommand@LST AMFDIALTEST
type: MMLCommand
name: LST AMFDIALTEST（查询AMF拨测用户配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFDIALTEST
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 灰度升级
- 拨测管理
status: active
---

# LST AMFDIALTEST（查询AMF拨测用户配置）

## 功能

**适用NF：MME、AMF**

该命令用于查询拨测用户配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEGINIMSI | 起始IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。不同记录的起始IMSI不能相同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFDIALTEST]] · AMF拨测用户配置（AMFDIALTEST）

## 使用实例

查询一条拨测用户配置，起始IMSI为460001111111111，执行如下命令：

```
%%LST AMFDIALTEST: BEGINIMSI="460001111111111";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
起始IMSI  =  460001111111111
终止IMSI  =  460001111111112
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFDIALTEST.md`
