---
id: UNC@20.15.2@MMLCommand@LST NGUSERNUMCTRL
type: MMLCommand
name: LST NGUSERNUMCTRL（查询5G接入用户数控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGUSERNUMCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 5G接入用户数控制
status: active
---

# LST NGUSERNUMCTRL（查询5G接入用户数控制参数）

## 功能

**适用NF：AMF**

该命令查询系统中当前配置的5G接入用户数控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：可选参数<br>参数含义：该参数表示需要限制接入漫游用户数的Serving PLMN。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>PLMNIDX已通过ADD NGSRVPLMN进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSERNUMCTRL]] · 5G接入用户数控制参数（NGUSERNUMCTRL）

## 使用实例

查询索引为1的ServingPLMN配置的接入用户数控制参数：

```
%%LST NGUSERNUMCTRL:PLMNIDX=1;%%
RETCODE = 0  操作成功

结果如下
--------
                PLMN索引  =  1
      漫游用户接入数上限  =  200000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGUSERNUMCTRL.md`
