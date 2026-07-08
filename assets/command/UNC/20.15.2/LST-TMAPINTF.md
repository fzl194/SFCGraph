---
id: UNC@20.15.2@MMLCommand@LST TMAPINTF
type: MMLCommand
name: LST TMAPINTF（查询Tm接口参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TMAPINTF
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口参数管理
status: active
---

# LST TMAPINTF（查询Tm接口参数）

## 功能

**适用NF：MME**

本命令用于查询Tm接口的管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [Tm接口参数（TMAPINTF）](configobject/UNC/20.15.2/TMAPINTF.md)

## 使用实例

查询Tm接口的管理参数记录：

LST TMAPINTF:;

```
%%LST TMAPINTF:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
Tm接口侦听端口号          =  29527   
Tm接口UDP校验功能         =  开启   
ECHO Request探测          =  开启   
ECHO探测间隔              =  60   
对端Recovery处理开关      =  开启   
过滤故障状态的Tm路径开关  =  开
容灾探测故障门限          =  4
TSN倒换等待时长（秒）     =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Tm接口参数(LST-TMAPINTF)_40967673.md`
