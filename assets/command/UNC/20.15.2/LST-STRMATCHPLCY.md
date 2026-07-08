---
id: UNC@20.15.2@MMLCommand@LST STRMATCHPLCY
type: MMLCommand
name: LST STRMATCHPLCY（查询字符串匹配策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STRMATCHPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 字符串匹配策略
status: active
---

# LST STRMATCHPLCY（查询字符串匹配策略）

## 功能

**适用NF：AMF**

该命令用于查询当前系统中配置的字符串匹配策略信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILEPATH | 文件路径 | 可选必选说明：可选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在文件的绝对路径。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| LINEPOS | 行号 | 可选必选说明：可选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在行号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STRMATCHPLCY]] · 字符串匹配策略（STRMATCHPLCY）

## 使用实例

显示系统中配置的字符串匹配规则，执行如下命令：

```
%%LST STRMATCHPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
      文件路径  =  b/test.go
          行号  =  100
字符串匹配策略  =  SENSITIVITY
        版本号  =  23.1.0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-STRMATCHPLCY.md`
