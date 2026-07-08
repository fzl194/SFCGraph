---
id: UNC@20.15.2@MMLCommand@LST GRPNGLANFUNC
type: MMLCommand
name: LST GRPNGLANFUNC（查询指定群组的5G LAN会话扩展参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GRPNGLANFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组级扩展功能
status: active
---

# LST GRPNGLANFUNC（查询指定群组的5G LAN会话扩展参数）

## 功能

**适用NF：SMF**

该命令用于查询指定会话组NGLAN扩展功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 5G LAN组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GRPNGLANFUNC]] · 指定群组的5G LAN会话扩展参数（GRPNGLANFUNC）

## 使用实例

查询当前系统中GROUPID为"A0000001-460-003-01"的5G LAN会话。

```
%%LST GRPNGLANFUNC:GROUPID="A0000001-460-003-01";%%
RETCODE = 0  操作成功

结果如下
--------
                        5G LAN组ID  =  A0000001-460-003-01
                   是否支持N19通信  =  不支持
        以太会话锚点重定位功能开关  =  不支持
               是否创建组播PDR规则  =  不支持
              是否支持N6侧上行广播  =  不支持
              是否支持报文增殖消除  =  不支持
                   MAC地址处理模式  =  MAC地址单条上报
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GRPNGLANFUNC.md`
