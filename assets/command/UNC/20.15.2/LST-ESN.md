---
id: UNC@20.15.2@MMLCommand@LST ESN
type: MMLCommand
name: LST ESN（查询网元中的设备序列号）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ESN
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# LST ESN（查询网元中的设备序列号）

## 功能

该命令用于查看网元中的设备序列号（ESN）。用户在向华为公司申请License文件前，需要使用该命令获取网元的ESN。使用该ESN申请到的License文件可以在该网元上激活。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ESN]] · 设备序列号（ESN）

## 使用实例

查询当前网元的设备序列号：

```
%%LST ESN:;%%
RETCODE = 0  操作成功

结果如下
--------
当前网元的设备序列号  =  RA2016010506592609A2212D74D821995C47
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ESN.md`
