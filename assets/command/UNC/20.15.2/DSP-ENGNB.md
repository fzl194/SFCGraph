---
id: UNC@20.15.2@MMLCommand@DSP ENGNB
type: MMLCommand
name: DSP ENGNB（显示en-gNB标识）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ENGNB
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- en-gNB 标识
status: active
---

# DSP ENGNB（显示en-gNB标识）

## 功能

**适用NF：MME**

查询系统中所有的en-gNB。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENGNB]] · en-gNB标识（ENGNB）

## 使用实例

查询系统中所有的en-gNB：

DSP ENGNB:;

```
%%DSP ENGNB:;%%
RETCODE = 0  操作成功

查询结果如下
------------
移动国家代码  移动网号  en-gNB标识  en-gNB ID有效比特长度  

263           127       14764        24                      
263           127       50778        24                      
263           127       50555        24                      
263           127       51001        24                      
263           127       50109        24                      
263           127       48315        24                      
263           127       49207        24                      
263           127       50332        24                      
263           127       48761        24                      
263           127       51224        24                      
(结果个数 = 10)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ENGNB.md`
