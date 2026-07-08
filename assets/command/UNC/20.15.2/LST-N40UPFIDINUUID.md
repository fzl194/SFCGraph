---
id: UNC@20.15.2@MMLCommand@LST N40UPFIDINUUID
type: MMLCommand
name: LST N40UPFIDINUUID（查询N40接口非UUID格式与UUID格式的UPF实例标识的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40UPFIDINUUID
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
- 计费管理
- 融合计费
- 全局配置
status: active
---

# LST N40UPFIDINUUID（查询N40接口非UUID格式与UUID格式的UPF实例标识的映射关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询N40接口非UUID格式与UUID格式的UPF实例标识的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~18。UPFINSTANCEID参数必须满足以下约束规则：1. 非UUID格式，不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF。2. 不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@N40UPFIDINUUID]] · N40接口非UUID格式与UUID格式的UPF实例标识的映射关系（N40UPFIDINUUID）

## 使用实例

查询N40接口非UUID格式的UPF实例标识"upfinstance1"映射的UUID格式UPF实例标识：

```
%%LST N40UPFIDINUUID: UPFINSTANCEID="upfinstance1";%%
RETCODE = 0  操作成功。

结果如下
------------------------
            UPF实例标识  =  upfinstance1
UPF实例标识的UUID格式值  =  00000000-0000-0000-0000-000000000001
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N40UPFIDINUUID.md`
